# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.database import Base  # noqa
from app.items.models import Item  # noqa
