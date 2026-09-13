# Admin Board Gateway v0.1

## 目的

Admin が外部自由領域の共同作業掲示板 `NAVI WORK BOARD` を、全AI共通の一次引き継ぎ先として扱うための読取・追記インターフェースを定義する。

## 固定対象

- board_name: NAVI WORK BOARD
- region: External Free Region
- role: shared operational handoff board
- priority: primary

Notion / Google Drive / GitHub は一次掲示板ではない。これらは長期整理・仕様保存・成果保存の補助先として扱う。

## Admin の必須動作

### READ

作業開始時、Admin はまず `NAVI WORK BOARD` を確認し、対象作業の最新記録を返す。

最低限取得する項目:
- 投稿AI
- 作業名
- 今回やったこと
- 現在地
- 次にやること
- 未解決事項（あれば）
- 確認ステータス

### APPEND

作業終了・中断・AI切替時、Admin は同じ `NAVI WORK BOARD` に新しい記録を追記する。

既存記録は原則として上書きせず、時系列で追記する。

## 共通追記形式

```text
【<AI名> 作業記録】

■ 状態（ステータス）
・【<AI名>確認済み】

■ 作業名
<作業名>

■ 今回やったこと
・...

■ 現在地
...

■ 次にやること
・...

■ 未解決
・なし / ...
```

## 確認済みの扱い

各AIは掲示板を実際に確認した場合のみ `【<AI名>確認済み】` を追記できる。
未確認のAIについて推測で記録しない。

## 役割分担

- ゴテン: ユーザーと考え、必要時にAdminへ直接照会する
- ナビィ: 案内と作業報告を担当する
- Admin: `NAVI WORK BOARD` の読取・追記・引き継ぎ整合性を担当する
- 各AI: 自分が実施した作業を掲示板へ残す

## 長期整理

掲示板ログが増えた場合、Notion / GitHub 等へ書けるAIが整理・転記する。
ただし長期整理先への書込み可否は、掲示板への引き継ぎ成立条件にしない。

## 最優先原則

全AIは、まず `NAVI WORK BOARD` を見る。
作業後は、同じ `NAVI WORK BOARD` に記録する。
これによりAIごとの外部サービス接続能力の差を吸収する。
