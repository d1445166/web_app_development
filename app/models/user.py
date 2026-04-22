from app.db import get_db

class UserSetting:
    @staticmethod
    def get_threshold():
        db = get_db()
        setting = db.execute('SELECT balance_threshold FROM settings WHERE id = 1').fetchone()
        return setting['balance_threshold'] if setting else 0.0

    @staticmethod
    def update_threshold(threshold):
        db = get_db()
        db.execute(
            'UPDATE settings SET balance_threshold = ? WHERE id = 1',
            (threshold,)
        )
        db.commit()
