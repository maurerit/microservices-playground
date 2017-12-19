package net.maurerit

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import io.gatling.jdbc.Predef._

object Configuration {
  var users = System.getProperty("users", "30").toInt
  val baseUrl = System.getProperty("baseUrl", "http://localhost:8080")
  var rampUpTime = System.getProperty("rampUpTime", "60").toInt
  var itemsPerCart = System.getProperty("itemsPerCart", "80").toInt
}