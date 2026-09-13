# 作業オブジェクト標準テンプレート v1.0

```yaml
work_id: UNIQUE-ID
title: 作業名
purpose: この作業の目的
status: ready
current_position: 現在どこまで進んでいるか
last_action: 最後に行った作業
next_action: 次に行う具体的な作業
unresolved:
  - 未解決事項
assigned_ai: 任意。固定しなくてよい
references:
  - 参照先URL、ファイル、Notion、GitHub等
updated_at: YYYY-MM-DD HH:MM TZ
```

## 詳細ログ

### Log Entry

- timestamp:
- actor:
- action:
- result:
- issue:
- next:

## 引き継ぎチェック

次のAIが以下を理解できるか確認する。

- 何をする作業か
- どこまで終わっているか
- 最後に何をしたか
- 次に何をするか
- 未解決事項は何か
- 必要な参照先はどこか

## 原則

作業オブジェクトはAIごとに作るのではなく、作業ごとに作る。

ChatGPTからGemini、GeminiからCopilotなど担当AIが変わっても、同じ作業であれば同一 work_id を引き継ぐ。

ユーザーが別の作業を始めた場合のみ、新しい作業オブジェクトを作成する。
