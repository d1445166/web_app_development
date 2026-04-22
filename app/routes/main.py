from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.record import Record
from app.models.user import UserSetting
from datetime import date

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def dashboard():
    today_str = date.today().strftime('%Y-%m-%d')
    today_records = Record.get_all(date=today_str)
    total_balance = Record.get_total_balance()
    threshold = UserSetting.get_threshold()
    
    return render_template(
        'index.html', 
        records=today_records, 
        total_balance=total_balance, 
        threshold=threshold,
        today=today_str
    )

@main_bp.route('/add', methods=['POST'])
def add_record():
    record_type = request.form.get('type')
    amount_str = request.form.get('amount')
    record_date = request.form.get('date') or date.today().strftime('%Y-%m-%d')
    description = request.form.get('description', '')

    if not record_type or record_type not in ['income', 'expense']:
        flash('無效的收支類型', 'danger')
        return redirect(url_for('main.dashboard'))

    try:
        amount = float(amount_str)
        if amount <= 0:
            raise ValueError
    except (TypeError, ValueError):
        flash('金額必須是大於 0 的數字', 'danger')
        return redirect(url_for('main.dashboard'))

    Record.create({
        'type': record_type,
        'amount': amount,
        'date': record_date,
        'description': description
    })
    
    flash('新增成功！', 'success')
    return redirect(url_for('main.dashboard'))

@main_bp.route('/delete/<int:id>', methods=['POST'])
def delete_record(id):
    Record.delete(id)
    flash('刪除成功！', 'success')
    referer = request.headers.get("Referer")
    if referer and 'history' in referer:
        return redirect(url_for('main.history'))
    return redirect(url_for('main.dashboard'))

@main_bp.route('/history', methods=['GET'])
def history():
    filter_date = request.args.get('date')
    records = Record.get_all(date=filter_date)
    return render_template('history.html', records=records, filter_date=filter_date)

@main_bp.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        threshold_str = request.form.get('balance_threshold')
        try:
            threshold = float(threshold_str)
            UserSetting.update_threshold(threshold)
            flash('警示底線設定已更新！', 'success')
            return redirect(url_for('main.dashboard'))
        except (TypeError, ValueError):
            flash('請輸入有效的數字', 'danger')
            
    current_threshold = UserSetting.get_threshold()
    return render_template('settings.html', current_threshold=current_threshold)
