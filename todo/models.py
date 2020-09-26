from django.db import models

# Create your models here.
        
#左側に表示される文字列、右側がそれをプログラム上で扱う文字列。
#ここでは左側の文字列はbootstrapのcssの色指定の文字列と連携させる
PRIORITY ={('danger','high'),('info','normal'),('success','low')}


class TodoModel(models.Model):
    #CharField：大文字小文字の文字列フィールド　ぐぐるといっぱいでてくる
    #max_lengthで長さを指定　指定しないとエラーになる
    title = models.CharField(max_length=100)
    #TextField:CharFieldより長い文章入れる用
    memo = models.TextField()
    #優先度は短い文字列
    priority = models.CharField(
        max_length=50,
        #choicesでタプル型の選択肢を作れる
        choices = PRIORITY
        )
    #日時はDateField
    duedate = models.DateField()
    #このモデルを文字列のオブジェクトとして返す
    #__str__ではタイトルの文字列を返すと一覧にタイトルが載るようになる
    def __str__(self):
        return self.title

    
    
#model.pyを作ったらmakemigrationsとmigrateをする
#makemaigrations:DBとの間のもう少し細かい設計図を作る。履歴が残るので失敗しても戻せる。エラー内容も表示してくれる。
#履歴は0001_initial.pyから番号順に作られる
#migrate：DBに反映する完了作業。最初はいろんなテーブルが作られる
#新たにカラムを追加してmakemigrationsするとターミナルに警告が出る
#null==Trueでnullを許容することができる。ターミナル上では1の選択肢
#1を選択すると自分で入れるものを入力させられる