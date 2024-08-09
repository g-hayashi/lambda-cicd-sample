# リポジトリ概要

このリポジトリには、lambdaのPythonコードと、CodeBuild/CodeDeployに利用可能なappspec.yamlとbuildspec.yamlが含まれています。
BuildSpecでLambdaへのAliasを利用したコードの更新を行い、AppSpecのバージョン記載を更新します。
これら全てのファイルをArtifactとし、CodeDeployでBLUE/GREENデプロイを可能にする簡単なサンプルです。

## 使用方法
デプロイが完了したら、AWS Lambdaコンソールから関数をテストするか、API Gatewayを設定してエンドポイントを呼び出します。

## 注意事項
- デプロイメントの詳細はAWSの公式ドキュメントを参照してください。
