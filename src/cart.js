let cartCount = 0;

export const addToCart = () => {
    cartCount++;
    updateCart();
}

export const getCartCount = () => {
    return cartCount;
}

const updateCart = () => {
    console.log(cartCount)
    document.dispatchEvent(new Event('cartUpdated')); // Dispara un evento para que los componentes escuchen los cambios
}