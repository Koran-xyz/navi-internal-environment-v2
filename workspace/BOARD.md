# 外部作業空間 共有掲示板 v1.0

この掲示板は、外部自由領域に存在する作業の現在地を一覧で確認するための索引である。

詳細履歴は各作業オブジェクトへ分離し、この掲示板には現在状態だけを簡潔に記録する。

## 最初に読むこと

すべてのAIは、新規・継続を問わず作業開始前にこの掲示板を確認する。
関連するWork Objectが存在する場合は、その記録とAdminの引き継ぎ情報を確認してから作業を開始する。

## 運用ルール

- 新しい作業が発生したら、既存作業の続きか確認する
- 続きなら既存の作業オブジェクトを更新する
- 別作業なら新しい work_id を作成する
- 作業中は節目で中間記録する
- 作業終了・中断・AI切替前は「現在地」「最後に行ったこと」「次に行うこと」を必ず更新する
- AIを変更しても、担当AI名だけを理由に作業を分割しない
- Adminは掲示板が現在状態と一致しているか確認する

## Active Work

| work_id | 作業名 | 状態 | 現在地 | 最後に行ったこと | 次に行うこと | 詳細 |
|---|---|---|---|---|---|---|
| NAVI-ADMIN-RUNTIME-001 | Admin 常駐ランタイム実装 | idea | v1.0本体から追加機能として分離済み | 常駐化要件を別Work Objectとして作成 | 最小要件を1つに絞り、無料/低コスト実行基盤を選ぶ | `workspace/work_objects/NAVI-ADMIN-RUNTIME-001.md` |

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
