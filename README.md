# Smart-Home-System

## Project Description
- [期間]：2022年5月30日から7月28日
- [企画概要]：
　生活するとき感じた面倒のもと、家の各所に散乱してる大勢の電気スイッチやリモコン。
その面倒感を解決するため、それぞれを一つのシステムに一括管理したいと思います。
そして、管理するたげで、スマートということにはまだ遠いですので、
もっとエンジニアポックスマートの生活をしていきたいため、自動化と音声認識機能も導入したいと思います。
- [開発環境]：
  - 中継機：
   - マイコン基盤：raspberry pi 3
   - 赤外線、センサーの開発言語：python 3.7
   - 自動化スクリプト：shell script
  - サーバ：
   - サーバインスタンス：DELL R620(web server, API serverなど), DELL R720(database server, storage server)
   - サーバOS:ESXi
   - サーバ群管理システム：vcsa
   - web server：CentOS 7, apache, php, HTML, CSS, JavaScritp , laravel8, bootstrap5
   - API server：python Flask
   - database server：Mysql
- [担当実績・取り組み]：
  - ハードウェアの組み込み：配線（赤外線発受信器、各センサー）、コーティング（赤外線発受信器、各センサー）
  - フロントアント：デザイン（システム、デジタルサイネージ全画面）、コーティング（システムのダッシュボードとオートコントロール画面）
  - バックアント：php、データベース作成
  - インフラ環境：firewall（ポリシーの設定, VPN設定）、switch（vlan, access port, trunk port設定）
　  - サーバー環境：DNS server 作成、AD server 作成、web server 作成、API server 作成、database server作成

## Directory Description
- document : 計画資料、開発経歴書
- presen : プレゼン資料
- project : 作品データ

## Team
| Member |  Lin   | Kimura | 
| ------ |:------:|:--------:|
| Duties |   PM/INFRA/frontend/backend    |    backend    | 
| Branch | master | master  | 

## Program Language
- front
	- HTLM, js
- back
	- PHP
	- laraval
	- Python

## Component
- 中継器（赤外線収発信機）
<img src="https://user-images.githubusercontent.com/84487405/232200743-517d10ed-d4cc-4f16-872c-9733521ed7ab.jpg" width = "auto" height = "200" alt="图片名称" align=center />
- デジタルサイネージ（屋内情報表示、リモコン登録）
<img src="https://user-images.githubusercontent.com/84487405/232200841-ea2ae98e-9d7d-4354-b1a6-e92c453c5c73.PNG" width = "auto" height = "200" alt="图片名称" align=center />
- システムダッシュボード（リモコン登録、家電コントロール、自動化、siri連携）
<img src="https://user-images.githubusercontent.com/84487405/232200967-aa793b61-f567-4300-a210-d1fbfc979164.png" width = "auto" height = "200" alt="图片名称" align=center />
- サーバ（VPNトンネル、mqtt、websocket、DB）
![サーバ3](https://user-images.githubusercontent.com/84487405/232202444-1cff4e59-b40f-4d42-9f24-f00c55b8ba37.jpg)





https://user-images.githubusercontent.com/84487405/230754995-fb837b3e-7c58-4d89-83eb-6d560e817288.mp4

