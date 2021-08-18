from datetime import datetime

from pytz import timezone

from app.core import db


class TimestampMixin(object):
    '''
    모델에 timestamp 생성
    '''
    created = db.Column(db.DateTime, default=datetime.now(timezone('Asia/Seoul')))
    modified = db.Column(db.DateTime, onupdate=datetime.now(timezone('Asia/Seoul')))


class BaseModel(TimestampMixin):
    '''
    model instance 관련 메소드가 추가된 BaseModel
    '''

    def update(self):
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
