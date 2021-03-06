package net.maurerit

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import io.gatling.jdbc.Predef._
import scala.concurrent.duration._
import scala.util.Random

class LoadSimulation extends Simulation {
  val httpProtocol = http
    .baseURL(Configuration.baseUrl)
    .inferHtmlResources()
    .acceptHeader("application/json")
    .acceptEncodingHeader("gzip, deflate")
    .acceptLanguageHeader("en-US,en;q=0.8")
    .userAgentHeader("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")

  object ShoppingCart {
    val headers = Map(
      "Content-Type" -> "application/json",
      "Origin" -> Configuration.baseUrl
    )

    val users = Iterator.continually(
      Map("userId" -> Random.nextLong())
    )
    val items = Iterator.continually(
      Map("itemId" -> Random.nextInt(100000))
    )
    val price = Iterator.continually(
      Map("price" -> Random.nextInt(6000000))
    )
    val quantity = Iterator.continually(
      Map("quantity" -> Random.nextInt(40))
    )

    val getCurrentCart = exec(
      http("get_current_cart")
        .post("/cart")
        .headers(headers)
        .body(StringBody("${userId}"))
        .check(jsonPath("$.shoppingCartId").saveAs("shoppingCartId"))
    )

    val getByCartId = exec(
      http("get_by_cart_id")
        .get("/cart/${shoppingCartId}")
        .headers(headers)
    )

    val addItemToCart = exec(
      http("add_item_to_cart")
        .post("/cart/${shoppingCartId}")
        .body(StringBody("""{ "itemId": ${itemId}, "price":${price}, "quantity":${quantity}, "status":"SHOPPING" }""")).asJSON
    )

    val checkout = exec(
      http("checkout")
        .patch("/cart/${shoppingCartId}")
    )
  }

  val cartOperations = scenario("Shop and checkout")
    .feed(ShoppingCart.users)
    .exec(
      ShoppingCart.getCurrentCart,
      ShoppingCart.getByCartId
    )
    .repeat(Configuration.itemsPerCart) {
      feed(ShoppingCart.items)
      .feed(ShoppingCart.price)
      .feed(ShoppingCart.quantity)
      .exec(
        ShoppingCart.addItemToCart
      )
    }
    .exec(
      ShoppingCart.checkout
    )

  setUp (
    cartOperations.inject(
      rampUsers(Configuration.users) over (Configuration.rampUpTime seconds)
    )
  ).protocols(httpProtocol)
}
