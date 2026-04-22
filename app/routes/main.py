from flask import Blueprint, render_template, request, redirect, url_for, abort

# 建立一個 blueprint 來管理主要路由
main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def dashboard():
    """
    儀表板首頁
    輸出渲染: templates/index.html
    邏輯:
      1. 取得當日所有收入與支出
      2. 取得歷史以來的總餘額
      3. 取得目前餘額底線設定以判斷是否需要觸發警示
    """
    pass

@main_bp.route('/add', methods=['POST'])
def add_record():
    """
    新增收支紀錄
    輸入參數: type, amount, date(可選), description(可選) 由 form data 提供
    輸出結果: 儲存成功後 redirect 至首頁 '/'
    邏輯:
      1. 驗證各欄位合法性 (確保 amount 數字且大於0)
      2. 寫入 DB 並重算該時間點相關設定
    """
    pass

@main_bp.route('/delete/<int:id>', methods=['POST'])
def delete_record(id):
    """
    刪除特定收支紀錄
    輸入參數: 紀錄 id (URL 參數)
    輸出結果: 刪除後 redirect 回先前發送請求的頁面
    邏輯:
      1. 檢查紀錄存在
      2. 給予刪除指令並操作 DB
    """
    pass

@main_bp.route('/history', methods=['GET'])
def history():
    """
    顯示歷史紀錄 (支援依照日期過濾)
    輸出渲染: templates/history.html
    輸入參數: date (Query String 可選參數)
    邏輯:
      1. 若有特定日期則依日期過濾紀錄
      2. 取得所有範圍內的收支明細
    """
    pass

@main_bp.route('/settings', methods=['GET', 'POST'])
def settings():
    """
    系統警示設定頁面 (讀取與更新)
    輸出渲染/結果: 
      - GET: 渲染 templates/settings.html 並顯示當前額度
      - POST: 驗證接收 form data 後更新至資料庫並 redirect 回 '/'
    邏輯:
      1. GET 時調用 model 讀取現有 threshold
      2. POST 時更新 model 內的儲存值
    """
    pass
