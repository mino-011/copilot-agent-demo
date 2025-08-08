# M365 Copilot Agent – Meeting Summary & Action Item Automation

This repository contains a sample design and prototype of a Microsoft 365 Copilot Agent for enterprise productivity in the Japanese market. 
The agent assists in automating meeting summarization and action item tracking by leveraging Azure OpenAI Service, Microsoft Graph API, and Power Platform connectors.

本リポジトリは、日本企業向けに設計したMicrosoft 365 Copilot Agentのサンプルプロジェクトです。
Azure OpenAI、Microsoft Graph API、Power Platformを活用し、会議の要約とアクションアイテム管理を自動化します。

##　Background
Meetings in Japan tend to be lengthy and creating meeting minutes and tracking tasks is often manual. This project demonstrates how Microsoft 365 Copilot can automate the entire workflow:
Meeting -> Summary Generation -> Task Creation

## 背景
日本企業では会議が長く、議事録作成やタスク化が属人的になりやすい課題があります。  
本プロジェクトでは、Microsoft 365 Copilot と AI を活用し、**「会議終了 → 要約生成 → タスク登録」**までの流れを自動化します。

## Flow
- Get Teams meeting transcripts via Microsoft GraphAPI
- Generate summary and action items using Azure OpenAI GPT-5
- Automatically registter tasks to Planner using Power Automate

## フロー
1. Teams 会議終了後、Microsoft Graph API で会議の文字起こしデータを取得
2. Azure OpenAI GPT-4 により要約とアクションアイテム抽出
3. Power Automate フローで Planner / To Do に自動登録

## Technical Stack
- Microsoft Graph API - Get meeting transcripts
- Azure OpenAI Service - Generate summaries and action items
- Power Automate - Task creation
-  Python - Data processing scripts
  
## 技術スタック
- Microsoft Graph API – 会議記録取得
- Azure OpenAI Service – 要約＆アクションアイテム生成
- Power Automate – タスク登録
- Python – データ取得・処理スクリプト
