package net.maurerit.shoppingcart.repo;

import net.maurerit.shoppingcart.domain.ShoppingCartItem;
import net.maurerit.shoppingcart.domain.ShoppingCartItemPK;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Created by MM66053 on 3/1/2017.
 */
@Repository
public interface ShoppingCartItemRepository extends JpaRepository<ShoppingCartItem, ShoppingCartItemPK>, BaseShoppingCartItemRepository {
}
