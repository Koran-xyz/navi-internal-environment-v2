# Work Object: NAVI-ADMIN-RUNTIME-001

## 基本情報

- work_id: NAVI-ADMIN-RUNTIME-001
- title: Admin 常駐ランタイム実装
- status: active
- purpose: ナビィシステム v1.0 の外部作業基盤上で、Adminが時間監視・中間保存・進行管理を継続的に行える実行基盤を追加する
- assigned_ai: ChatGPT / ゴテン
- updated_at: 2026-09-14

## 現在地

外部自由領域の共同作業掲示板を `NAVI WORK BOARD` として固定し、Admin がこの掲示板を一次引き継ぎ先として READ / APPEND するための gateway 仕様を追加した。

実装済み:
- `agents/admin/board_gateway.md`
- ゴテン → Admin 直接照会プロトコル
- 共通掲示板追記形式

未実装:
- このChatGPT実行環境から外部自由領域の実掲示板へ直接 READ / APPEND する実行コネクタ

## 必要機能

- `NAVI WORK BOARD` の直接読取
- `NAVI WORK BOARD` への直接追記
- 一定時間無操作時の中間保存
- 未記録作業の検出
- 次回引き継ぎに必要な状態整理
- 必要に応じて大型AIへ処理を委譲

## 次に行うこと

1. 外部自由領域の実掲示板に対する実行コネクタを接続する
2. `READ NAVI WORK BOARD` をテストする
3. ChatGPT / ゴテン名義で `【ChatGPT確認済み】` を実掲示板へ追記する
4. 追記後に再読取して反映を確認する

## 参照先

- `NAVI_SYSTEM_V1.md`
- `agents/admin/board_gateway.md`
- `agents/goten/direct_admin_protocol.md`
- `agents/admin/admin_rules.md`
