from datetime import datetime, timedelta

from model.base import Base, db
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, text
from sqlalchemy.orm import aliased, relationship


class UserActivity(Base, db.Model):
    __tablename__ = "user_activity"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    action = Column(
        String(50)
    )  # Action description, e.g., "login", "view_record", etc.
    details = Column(String(255))  # Additional details about the action

    user = relationship("User", back_populates="activities")

    @classmethod
    def calculate_last_30_days_activity(cls):
        """
        Calculate the number of actions performed daily for the last 30 days.

        :return: List of dictionaries with 'date' and 'count'
        """
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=30)

        daily_activity = (
            UserActivity.query.filter(
                UserActivity.created_at >= start_date,
                UserActivity.created_at <= end_date,
            )
            .group_by(func.date(UserActivity.created_at))
            .with_entities(
                func.date(UserActivity.created_at).label("date"),
                func.count().label("count"),
            )
            .all()
        )

        return [{"date": str(date), "count": count} for date, count in daily_activity]

    @classmethod
    def calculate_last_24_hours_activity(cls):
        """
        Calculate the number of actions performed every 15 minutes for the last 24 hours.

        :return: List of dictionaries with 'time' and 'count'
        """
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(hours=24)

        hourly_activity = (
            UserActivity.query.filter(
                UserActivity.created_at >= start_time,
                UserActivity.created_at <= end_time,
            )
            .group_by(
                func.date_format(UserActivity.created_at, "%Y-%m-%d %H:00:00").label(
                    "time"
                ),
                func.date_format(UserActivity.created_at, "%Y-%m-%d %H:%i:00").label(
                    "minute"
                ),
            )
            .with_entities(
                func.date_format(UserActivity.created_at, "%Y-%m-%d %H:%i:00").label(
                    "minute"
                ),
                func.count().label("count"),
            )
            .all()
        )

        return [{"time": str(time), "count": count} for time, count in hourly_activity]

    @classmethod
    def get_most_active_hours(cls, limit=5):
        """
        Get the most active hours in the last 30 days.

        :param limit: Number of hours to retrieve (default: 5)
        :return: List of dictionaries with 'hour' and 'count'
        """
        active_hours = (
            db.session.query(
                func.HOUR(cls.created_at).label("hour"), func.count().label("count")
            )
            .filter(cls.created_at >= datetime.utcnow() - timedelta(days=30))
            .group_by(func.HOUR(cls.created_at))
            .order_by(func.count().desc())
            .limit(limit)
            .all()
        )

        return [{"hour": hour, "count": count} for hour, count in active_hours]

    @classmethod
    def get_least_active_hours(cls, limit=5):
        """
        Get the bottom N hours with the least activity in the last 30 days.

        :param limit: Number of bottom hours to retrieve
        :return: List of dictionaries with 'hour' and 'count'
        """
        least_active_hours = (
            db.session.query(
                func.HOUR(cls.created_at).label("hour"),
                func.count().label("count"),
            )
            .filter(cls.created_at >= datetime.utcnow() - timedelta(days=30))
            .group_by(func.HOUR(cls.created_at))
            .order_by(func.count().asc())
            .limit(limit)
            .all()
        )

        return [{"hour": hour, "count": count} for hour, count in least_active_hours]

    @classmethod
    def get_dead_hours(cls, limit=5):
        """
        Get hours with next to zero activity in the last 30 days.

        :return: List of hours with next to zero activity
        """
        all_hours = set(range(24))
        active_hours = (
            db.session.query(func.HOUR(cls.created_at).label("hour"))
            .filter(cls.created_at >= datetime.utcnow() - timedelta(days=30))
            .group_by(func.HOUR(cls.created_at))
            .all()
        )

        active_hours = set(hour[0] for hour in active_hours)

        dead_hours = list(all_hours - active_hours)[1 : limit + 1]

        return dead_hours
