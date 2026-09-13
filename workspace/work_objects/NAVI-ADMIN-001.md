# Work Object: NAVI-ADMIN-001

## 基本情報

- work_id: NAVI-ADMIN-001
- title: 外部自由領域 Admin 実装
- status: in_progress
- purpose: どのAIを使っても前回の続きから作業できるよう、外部自由領域に常駐型進行役Adminと共通引き継ぎ運用を実装する
- assigned_ai: 任意の対応AI
- updated_at: 2026-09-14

## 現在地

Adminの役割を「外部自由領域・外部作業空間の常駐型進行役」として固定済み。ナビィは各AI側の案内役、Adminは外部作業空間の進行・引き継ぎ管理役として分離した。

全AI共通の必須運用として、作業開始前に掲示板と関連Work Objectを確認し、作業中は節目ごとに記録し、終了・中断・AI切替前には引き継ぎ情報を残す方針を正式化した。

## 直近で行ったこと

- `agents/admin/admin_definition.md` をAdminの常駐型進行役定義へ更新
- `agents/admin/admin_rules.md` を引き継ぎ責任者として更新
- `workspace/BOARD.md` を作成
- `workspace/work_object_template.md` を作成
- `agents/navi/startup_handoff_protocol.md` を作成
- `workspace/handoff_protocol.md` を作成
- `workspace/mandatory_operation_protocol.md` を作成
- 「読む → 確認する → 作業する → 記録する → 引き継ぐ」を全AI共通必須フローとして固定
- 電話、寝落ち、アプリ終了など突然の中断を前提とし、途中記録を標準とする方針を確認

## 未解決

- Adminを実際のクラウド常駐型エージェントとして動かす実装方法は未確定
- 一定時間ユーザー入力がない場合の自動中間保存は、常駐実行基盤ができるまでは未実装
- 既存プロジェクト（Miy.Mid、Premiere Connector、旅行プラン等）のWork Object棚卸しが未実施
- 各AIが掲示板確認・途中記録・終了記録を本当に守るかの実運用テストが必要

## 次に行うこと

1. 1つの実作業を選び、別AI間で引き継ぎテストを実施する
2. 開始前掲示板確認 → Work Object読込 → 作業 → 中間記録 → 終了記録の一周を検証する
3. 既存作業をWork Objectとして棚卸しする
4. Adminの常駐実装候補（ローカル小型AI、クラウド小型エージェント等）を別途検討する

## 参照先

- `workspace/BOARD.md`
- `workspace/work_object_template.md`
- `workspace/handoff_protocol.md`
- `workspace/mandatory_operation_protocol.md`
- `agents/admin/admin_definition.md`
- `agents/admin/admin_rules.md`
- `agents/navi/startup_handoff_protocol.md`

## 引き継ぎメモ

この作業を再開するAIは、最初に `workspace/BOARD.md` と本Work Objectを読むこと。新しい独自構造を先に作らず、現在の共通運用ルールを基準に作業を継続すること。
