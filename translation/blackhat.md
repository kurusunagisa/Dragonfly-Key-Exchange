# dragonflyの仕組み

1. それぞれが，パスワードから群要素Pをつくる
2. Commitフェーズ
   1. 交渉された(ここでは共有でもいいかも)鍵を交渉する
3. Confirmフェーズ
   1. 交渉された鍵が同じ鍵かどうかを確認する
4. これらを行うために2つの暗号群がサポートされている
   1. MODP群
   2. Elliptic群

# MODP群とは

# xの場所

1. x < p (pは素数)
2. x^q mod p = 1
3. q = #elements in the group(意味が分からない……)
   多分qは群要素の中にあるってことだと思います

- All operations are MODulo the Primeの略がMODP
  - (全ての操作は素数の法)


# パスワードをMODP要素に変換する

```python
value = hash(pw, counter, addr1, addr2)

P = value^((p-1)/q)
return P
```

この操作でvalueをMODP要素に変換する

# サイドチャネル攻撃

しかし，群が22-24のとき，value >= pとなってしまう問題がある

```python
for (counter = 1; counter < 256; counter++)
    value = hash(pw, counter, addr1, addr2)
    if value > p: continue
    P = value^((p-1)/q)
    return P
```

繰り返しはパスワードに依存する

IETFとCFRGの警告があったにもかかわらず，タイミングリーク対策がない．

サイドチャネル攻撃に影響を受けやすく，もしかしたらパスワードをリークされてしまうかもしれない

些細な攻撃では，共有されたパスワードをリークすることはできないことがどのくらい重要かはよくわからないけど．．．

```python
for (counter = 1; counter < 256; counter++)
    value = hash(pw, counter, addr1, addr2)
```

addr1とaddr2はクライアントアドレス(俗に言うMACアドレス)

MACアドレスをなりすましてその異なる実行を入手すれば新しいデータをリークできる

RockYou dumpの中でパスワードを決定するためには17以下のアドレスが必要

Hostap APは~75　[measurements / address]

# 楕円曲線とは？

1. x < p かつ y < p (pは素数)
2. y^2 = x^3 + ax + b mod p

- パスワードを曲線上の点(x,y)に変換する必要がある

```python
for (counter = 1; counter < 40; counter++)x=        hash(pw, counter, addr1, addr2)
    #if x>= p: continue
    if square_root_exists(x) :
        return (x, sqrt(x^3+a*x+𝑏))
```

EAP-pwdは楕円曲線のタイミングリークと似ている

```python
for (counter = 1; counter < 40; counter++)x=        hash(pw, counter, addr1, addr2)
    #if x>= p: continue
    if square_root_exists(x) and not P:
        P = (x, sqrt(x^3+a*x+𝑏))
return P
```

WPA3はいつも40回ループして最初のPを返す

Brainpool曲線の問題として，x >= pの場合が存在する

```python
for (counter = 1; counter < 40; counter++)x=        hash(pw, counter, addr1, addr2)
    if x>= p: continue
    if square_root_exists(x) and not P:
         P = (x, sqrt(x^3+a*x+𝑏))
return P
```

こうすると，

```python
if square_root_exists(x) and not P:
         P = (x, sqrt(x^3+a*x+𝑏))
```

がスキップされてしまうことがある

掛け算(aPのときのa)のスキップはパスワードに依存する

クライアントMACアドレスの実行時間はパスワードの署名をつくる

# Cache Attacks

## NIST Elliptic Curves



