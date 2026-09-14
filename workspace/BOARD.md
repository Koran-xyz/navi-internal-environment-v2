# NAVI WORK BOARD｜外部作業空間 共有掲示板 v1.1

この掲示板は、外部自由領域に存在する作業の現在地を一覧で確認するための全AI共通の一次掲示板である。

## 正本位置

- Display Name: `NAVI WORK BOARD`
- Repository: `Koran-xyz/navi-internal-environment-v2`
- Path: `workspace/BOARD.md`
- Region: External Free Region / 外部自由領域

すべてのAIは、作業開始時にまずこの掲示板を確認し、作業終了・中断・AI切替時には最低限の引き継ぎ記録をこの掲示板へ残す。

Notion、Google Drive、その他の外部保存先は一次掲示板ではない。ログが蓄積した後、書き込み可能なAIが必要に応じて整理・保存する。

## 最初に読むこと

すべてのAIは、新規・継続を問わず作業開始前にこの掲示板を確認する。
関連するWork Objectが存在する場合は補助情報として参照するが、引き継ぎ成立の最低条件は、この掲示板に必要な記録が残っていることである。

## 共通記録の最低形式

- AI名
- 今回やったこと
- 現在地
- 次にやること
- 必要なら参照先

AIごとに別掲示板を作らず、同じ `NAVI WORK BOARD` に時系列で追記する。

## AI確認状態

- 【Gemini確認済み】
- 【ChatGPT確認済み】
- Copilot: 作業記録あり（自動運転AI制御・研究 / Copilot連携）

## ChatGPT / ゴテン 作業記録

- 作業確認: 完了
- 共有掲示板特定: 完了
- 今回やったこと: 外部自由領域の共同作業掲示板を特定し、`NAVI WORK BOARD` を全AI共通の作業確認・引き継ぎ場所として固定
- 現在地: ChatGPT / Gemini / Copilot の共通掲示板運用を確認済み
- 次にやること: 各AIは作業開始時にこの掲示板を確認し、終了・中断時に同じ掲示板へ追記する

## 運用ルール

- 新しい作業が発生したら、まず掲示板に記録する
- 既存作業の続きなら、その続きであることが分かるように追記する
- Work Objectを直接更新できないAIでも、掲示板に必要な引き継ぎ記録が残れば引き継ぎ成立とする
- 作業中は節目で中間記録する
- 作業終了・中断・AI切替前は「今回やったこと」「現在地」「次にやること」を最低限残す
- AIを変更しても、担当AI名だけを理由に作業を分割しない
- Adminは掲示板が現在状態と一致しているか確認する

## Active Work

| work_id | 作業名 | 状態 | 現在地 | 最後に行ったこと | 次に行うこと | 詳細 |
|---|---|---|---|---|---|---|
| NAVI-ADMIN-RUNTIME-001 | Admin 常駐ランタイム実装 | active | NAVI WORK BOARDを全AI共通の一次掲示板として固定 | 掲示板の正本位置とAI確認状態を確定 | 各AIで同じBOARDを読んで追記できる運用を継続検証 | `workspace/work_objects/NAVI-ADMIN-RUNTIME-001.md` |
| MIY-MID-STUDIO-001 | MIY.MID Studio 統合アプリ | active | 3タブ統合版 v0.2 をGitHub Pagesへ公開済み | プロンプト・合成・動画の3モードを1つに統合し、`Koran-xyz/-mid-trace` の `index.html` を更新 | 新しいチャットで実機テストを継続し、必要なら保存・履歴・テンプレート等を検討。ただしシンプルさを優先し機能追加は慎重に行う | 公開URL: `https://koran-xyz.github.io/-mid-trace/` |

## Latest Handoff｜MIY.MID Studio

- AI名: ChatGPT / ゴテン
- 日付: 2026-09-15
- 作業名: MIY.MID Studio 統合
- 今回やったこと:
  - 既存の静止画プロンプト、2画像合成、動画エフェクト機能を1アプリへ統合。
  - 上部タブを `プロンプト / 合成 / 動画` の3つに固定。
  - プロンプトタイプは機能を絞り、基本構成を整えた後にユーザーが自由コメントで追加指示できる設計。
  - 合成タイプはMID.Traceで検証した短いMidjourney向け構成を採用。2枚目を「エフェクト」として扱う。
  - 動画タイプは既存のエフェクト生成を統合。Saber系表現が特に有効で、自然な量から強い演出まで使い分け可能。
  - GitHub Pages公開先 `Koran-xyz/-mid-trace` の `index.html` を統合版 v0.2 に更新済み。
- 現在地:
  - 公開URL: `https://koran-xyz.github.io/-mid-trace/`
  - アプリは「作る・合成する・動かす」の3工程で利用可能。
  - プロンプト生成部分はAI APIではなくJavaScriptテンプレート方式。高速・無料・API不要・出力が安定するのが利点。
  - コアユーザーは生成されたプロンプトを土台に、自分で追記して高度化できる。
  - 合成では文字も比較的きれいに扱え、広告・SNS・店舗宣伝など応用幅が広い。
  - Saber系はAfter Effectsを使わずとも強い演出が作れる可能性があり、主力機能候補。
- 重要な判断:
  - 機能を増やしすぎず、シンプルさを維持する。
  - 初心者はそのまま使え、上級者は自由コメントや追記で拡張できる二層構造を維持。
  - 企業AI活動では「AI画像生成ツール」より「AI制作の指示設計ツール / 制作補助オプション」として扱う方向が有望。
- 次にやること:
  - 新しいチャットでSafari実機テストを継続。
  - 3タブの操作感、コピー、画像読み込み、動画プロンプトの挙動を確認。
  - 問題がなければ企業向けオプションとして説明文・用途例・導入手順をまとめる。
  - 保存・履歴・テンプレート呼び出しは候補だが、必要性を確認してから追加する。
- 注意:
  - iPhoneでコード本体を手編集させない。GitHub更新はゴテン側で行い、ユーザーはSafariでテストする役割分担を維持。
  - MID.Trace単体の旧画面に戻さず、今後は統合版を正として扱う。

## Completed Work

| work_id | 作業名 | 状態 | 完了内容 | 詳細 |
|---|---|---|---|---|
| NAVI-ADMIN-001 | ナビィ外部作業基盤 v1.0 | completed | ナビィ・Admin・掲示板・Work Object・開始/途中/終了/引き継ぎの共通運用仕様を完成 | `workspace/work_objects/NAVI-ADMIN-001.md` |

## System Specification

- 正本: `NAVI_SYSTEM_V1.md`
- 全AI必須運用: `workspace/mandatory_operation_protocol.md`
- 引き継ぎ手順: `workspace/handoff_protocol.md`
- ナビィ起動時: `agents/navi/startup_handoff_protocol.md`
- Adminルール: `agents/admin/admin_rules.md`
- ゴテン→Admin直接照会: `agents/goten/direct_admin_protocol.md`
- Admin BOARD Gateway: `agents/admin/board_gateway.md`

## Status Values

- idea
- ready
- in_progress
- waiting
- blocked
- review
- completed
- archived

## Admin Check

アドミンは、各作業について最低限以下が分かる状態を維持する。

- 目的
- 現在地
- 最後に行ったこと
- 次に行うこと
- 未解決事項
- 参照先
