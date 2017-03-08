package net.maurerit.shoppingcart.repo;

import net.maurerit.shoppingcart.domain.ShoppingCart;
import net.maurerit.shoppingcart.domain.ShoppingCartStatus;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

/**
 * Created by mm66053 on 2/28/2017.
 */
@Repository
public interface ShoppingCartRepository extends JpaRepository<ShoppingCart,Long>, BaseShoppingCartRepository {
    @Query("select coalesce(max(sc.shoppingCartId), 1) from ShoppingCart sc where sc.customerId = :customerId")
    Integer nextIdForCustomer ( @Param("customerId") Long customerId );
}
