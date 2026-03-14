import logging

logger = logging.getLogger(__name__)

def check_low_stock(product):
    if product.quantity < product.threshold:
        logger.warning(
            f"Low Stock Alert: {product.name} only has {product.quantity} left!"
        )