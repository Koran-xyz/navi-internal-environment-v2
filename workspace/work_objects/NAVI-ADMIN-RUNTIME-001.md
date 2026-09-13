# Work Object: NAVI-ADMIN-RUNTIME-001

## 基本情報

- work_id: NAVI-ADMIN-RUNTIME-001
- title: Admin 常駐ランタイム実装
- status: idea
- purpose: ナビィシステム v1.0 の外部作業基盤上で、Adminが時間監視・中間保存・進行管理を継続的に行える実行基盤を追加する
- assigned_ai: 未定
- updated_at: 2026-09-14

## 現在地

ナビィシステム v1.0 の運用仕様は完成済み。
本Work Objectは、その上に追加する常駐実行機能を別機能として管理する。

## 候補

- ローカル小型AI + Python
- LM Studio / Ollama 等のローカル推論基盤
- クラウド小型AI
- 外部ジョブ / スケジューラ

## 必要機能

- 一定時間無操作時の中間保存
- BOARD / Work Object の定期確認
- 未記録作業の検出
- 次回引き継ぎに必要な状態整理
- 必要に応じて大型AIへ処理を委譲

## 次に行うこと

1. 最小要件を1つに絞る
2. 無料または低コストの実行基盤を選ぶ
3. 「作業ログを読む → 次作業を1件返す」だけの最小Adminを試作する
4. v1.0本体を変更せず追加できることを確認する

## 参照先

- `NAVI_SYSTEM_V1.md`
- `workspace/BOARD.md`
- `agents/admin/admin_rules.md`
