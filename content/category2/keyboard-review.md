Title: 가나다라마바사 아자차카타하
Date: 1010-12-03 10:20
Modified: 2010-12-05 19:30
Tags: pelican, publishing, verylonglongtag, aaaaaaaaaaaaaabd
Slug: 1234562
Authors: abc
Summary: Short version for index and feeds

최근에 한국어 텍스트 분석을 연습할 수 있는 데이터를 공유하고 있습니다. 데이터 분석 연습의 첫 코드가 분석이 아닌 데이터 수집이지 않기를 바래서 였습니다. 데이터셋의 구성과 앞으로 추가하려는 종류의 데이터, 그리고 연습 가능한 문제들을 살펴봅니다.

Textmining dataset
성능 평가까지 가능한 공개된 데이터들은 머신러닝과 자연어처리 분야의 발전에 큰 기여를 하였습니다. 분명 컴퓨터 비전 분야의 경우에는 ImageNet 데이터를 이용한 competition 이 모델의 발전을 촉진했습니다. 특정 tasks 를 위한 labeled data 가 있다면 기존 알고리즘과 비교하며 새로운 알고리즘의 성능을 객관적으로 평가할 수 있습니다. NLP 에서도 CoNLL 의 shared task dataset 이 공개되어 있으며, 질의 응답 분야도 SQuAD dataset 이 발전에 큰 기여를 하였습니다. 그리고 각 테스크 별로 잘 정의된 데이터셋이 공유되고 있습니다. 이런 정리들은 여러 사람들이 정리하여 블로그나 github 에 공유되고 있기도 합니다.

최근에는 한국어 질의 응답용 KorQuAD 데이터도 공유되었습니다. 이전에도 한국어 감성 분석 (sentiment analysis) 을 위하여 네이버 영화 리뷰를 정리해둔 Naver sentiment movie corpus v1.0 이 공유되기도 했습니다.

이처럼 객관적인 성능을 평가할 수 있는 데이터도 필요하지만, 데이터 분석 공부를 시작할 때에도 손쉽게 접근할 수 있는 데이터셋이 여러 종류가 있다면 좋을 것입니다. 영화 리뷰, 뉴스, 뉴스 댓글 등 우리가 접근할 수 있는 데이터들은 많지만, 이 데이터들은 우리가 수집을 해야만 합니다. 처음 데이터 분석을 시작하려 할 때, 분석 코드가 아닌 데이터 수집 코드부터 작성하는 모습을 종종 보곤 했습니다. 데이터 분석을 하고 싶다면 첫 코드가 데이터 분석이었으면 좋겠습니다.

이러한 목적에서 수집된 한글 텍스트 데이터를 공유하는 작업을 진행하고 있습니다. 그리고 이 데이터를 이용한 usages 도 공유하려 하고 있습니다. 데이터셋의 repository 는 github.com/lovit/textmining_dataset 입니다. 그리고 이를 이용하는 textmining tutorial 을 github.com/lovit/python_ml4nlp 에 올리고 있습니다.

[Alt Text]({static}/assets/images/Jellyfish.jpg)