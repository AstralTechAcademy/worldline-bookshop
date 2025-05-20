let cartCount = Number(0);

export const addToCart = (amount) => {
    //cartCount++;
    cartCount += Number(amount)
    console.log(cartCount)
    document.dispatchEvent(new Event('cartUpdated')); // Dispara un evento para que los componentes escuchen los cambios
}

export const getCartCount = () => {
    return cartCount;
}

const updateCart = () => {
    console.log(cartCount)
    document.dispatchEvent(new Event('cartUpdated')); // Dispara un evento para que los componentes escuchen los cambios
}