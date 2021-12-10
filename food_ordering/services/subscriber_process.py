import logging
from food_ordering.models.order import OrderModel
logger = logging.getLogger(__name__)


class ProcessService(object):
    def process_order(obj):
        """
        process received message state WAITING -> APPROVED
        :return: TRUE if there is no error else FALSE
        """
        try:
            OrderModel.objects.filter(id=obj['obj_id']).update(status=OrderModel.STATUS_APPROVED)
        except Exception as e:
            logger.error("Error while updating order status detail: {}".format(e))
            return False
        return True
