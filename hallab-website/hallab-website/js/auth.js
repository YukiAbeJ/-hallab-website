/* ============================================================
   HAL Lab. — Authentication Utilities
   ============================================================
   セキュリティ仕様:
   - パスワードはWeb Crypto API (SHA-256) でハッシュ化（ユーザー名でソルト）
   - メンバー情報はlocalStorage（デバイスごと）
   - セッションはsessionStorage（ブラウザを閉じると失効）
   - セッション有効時間: 8時間
   ============================================================ */

const Auth = (() => {
  const MEMBERS_KEY = 'hallab_members_v1';
  const SESSION_KEY = 'hallab_session_v1';
  const SESSION_MS  = 8 * 60 * 60 * 1000; // 8 hours

  /* SHA-256 ハッシュ (Web Crypto API) */
  async function sha256(str) {
    const buf = await crypto.subtle.digest(
      'SHA-256', new TextEncoder().encode(str)
    );
    return Array.from(new Uint8Array(buf))
      .map(b => b.toString(16).padStart(2, '0')).join('');
  }

  /* パスワードハッシュ（名前でソルト） */
  async function hashPassword(name, password) {
    return sha256(password + '::hallab::' + name);
  }

  /* メンバーリスト取得 */
  function getMembers() {
    try { return JSON.parse(localStorage.getItem(MEMBERS_KEY) || '[]'); }
    catch { return []; }
  }

  /* メンバーリスト保存 */
  function saveMembers(list) {
    localStorage.setItem(MEMBERS_KEY, JSON.stringify(list));
  }

  /* セッション取得（期限切れはnull） */
  function getSession() {
    try {
      const s = JSON.parse(sessionStorage.getItem(SESSION_KEY));
      if (s && s.expiry > Date.now()) return s;
      sessionStorage.removeItem(SESSION_KEY);
      return null;
    } catch { return null; }
  }

  /* セッション作成 */
  function setSession(name) {
    sessionStorage.setItem(SESSION_KEY, JSON.stringify({
      name,
      loginTime: Date.now(),
      expiry: Date.now() + SESSION_MS
    }));
  }

  /* ログアウト */
  function logout() {
    sessionStorage.removeItem(SESSION_KEY);
  }

  /* 新規登録（招待コード検証後に呼び出す） */
  async function register(name, password) {
    if (!name || !password) return { ok: false, msg: 'お名前とパスワードを入力してください' };
    if (password.length < 8) return { ok: false, msg: 'パスワードは8文字以上で設定してください' };
    const hash = await hashPassword(name, password);
    const members = getMembers();
    const idx = members.findIndex(m => m.name === name);
    if (idx >= 0) {
      // 再登録（パスワードリセット）
      members[idx].passHash = hash;
      members[idx].updatedAt = Date.now();
    } else {
      members.push({ name, passHash: hash, registeredAt: Date.now() });
    }
    saveMembers(members);
    setSession(name);
    return { ok: true };
  }

  /* ログイン */
  async function login(name, password) {
    if (!name || !password) return { ok: false, msg: 'お名前とパスワードを入力してください' };
    const hash = await hashPassword(name, password);
    const members = getMembers();
    const member = members.find(m => m.name === name && m.passHash === hash);
    if (!member) return { ok: false, msg: 'お名前またはパスワードが正しくありません' };
    setSession(name);
    return { ok: true };
  }

  /* 認証必須ページ用チェック（未ログインなら即リダイレクト） */
  function requireAuth(redirectTo) {
    const s = getSession();
    if (!s) { window.location.replace(redirectTo || 'login.html'); return null; }
    return s;
  }

  return { register, login, logout, getSession, requireAuth };
})();
