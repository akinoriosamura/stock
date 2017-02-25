# stock
## Goal
create script for automatically predicting stock change.

### architecture
 - data_process
 - predict change(machine learning model)
 - share the redult 

### plan
 - use classification model
 - use regression model
 - expand to use automatically deal.

### classsification model(plan)
 - RandomForest
 - RNN
 - LSTM
 - CNN
 - CNN + LSTM
 - QRNN
 - GatedCNN
 - and so on


I will refer in below site

QRNN
https://arxiv.org/pdf/1611.01576.pdf

GatedCNN
https://arxiv.org/pdf/1612.08083.pdf

CNN で 時系列データ の 特徴量（特徴マップ） を 畳み込み で 抽出して、 + プーリング で 情報圧縮 する 方法 いろいろ
http://qiita.com/HirofumiYashima/items/91b3aade0d7c5b2d403b

【 調査 】CNN（Convolution Neural Net）を 用いた 時系列データの予測タスク、分類タスク 応用事例
http://qiita.com/HirofumiYashima/items/9b5cca736172161aae2a

【深層学習 で 多変量時系列解析】Deep Neural Network で 多変量の時系列データ を 使って、 分類予測・回帰予測する方法
http://qiita.com/HirofumiYashima/items/1cab35e27d765f08499e
