from sqlalchemy import Column, Integer, Float, String, ForeignKey, Boolean

from cellphonedb.core.models import Base


class Interaction(Base):
    __tablename__ = 'interaction'

    id_interaction = Column(Integer, nullable=False, primary_key=True)

    multidata_1_id = Column(Integer, ForeignKey('multidata.id_multidata'), nullable=False)
    multidata_2_id = Column(Integer, ForeignKey('multidata.id_multidata'), nullable=False)

    score_1 = Column(Float)
    score_2 = Column(Float)

    source = Column(String)
    comments_interaction = Column(String)
    family = Column(String)
    dlrp = Column(Boolean)
    iuhpar = Column(Boolean)

    is_cellphonedb_interactor = Column(Boolean)
