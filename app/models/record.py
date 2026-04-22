from app.db import get_db

class Record:
    @staticmethod
    def create(data):
        db = get_db()
        db.execute(
            'INSERT INTO records (type, amount, date, description) VALUES (?, ?, ?, ?)',
            (data['type'], data['amount'], data['date'], data.get('description', ''))
        )
        db.commit()

    @staticmethod
    def get_all(date=None):
        db = get_db()
        if date:
            records = db.execute(
                'SELECT * FROM records WHERE date = ? ORDER BY date DESC, id DESC',
                (date,)
            ).fetchall()
        else:
            records = db.execute(
                'SELECT * FROM records ORDER BY date DESC, id DESC'
            ).fetchall()
        return records

    @staticmethod
    def delete(id):
        db = get_db()
        db.execute('DELETE FROM records WHERE id = ?', (id,))
        db.commit()

    @staticmethod
    def get_total_balance():
        db = get_db()
        result = db.execute(
            "SELECT "
            "SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) - "
            "SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) as total "
            "FROM records"
        ).fetchone()
        return result['total'] if result['total'] is not None else 0.0
