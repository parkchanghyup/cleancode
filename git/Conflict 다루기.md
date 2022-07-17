# Conflict 다루기  

## Merge 과정에서 충돌이 발생할 때

일반적으로 같은 파일에서 같은 라인을 변경한 두 커밋들을 병합(merge)하면 충돌(conflict)가 발생한다.  
충돌이 발생하면 



```
<<<<<<< HEAD
first line
=======
new line
>>>>>>> ozm21q4 (conflict2 파일을 추가한다)
```

- `<<<<<<< HEAD`와 `=======` 사이에 있는 변경사항이 merge를 진행한 브랜치의 커밋 변경사항입니다
- `=======`와 `>>>>>>>{커밋 해시}` 사이에 있는 변경사항은 merge할 타겟 브랜치의 커밋 변경사항입니다.

충돌을 해결하기 위해선, 위에 있는 conflict marker를 지워주고 어떤 변경사항을 채택할지 결정하면 된다.  

```
# 충돌 해결 후
$ git add .
$ git commit
```  

## 하나의 브랜치를 함께 사용하다가 충돌이 나는 경우  

A와 B가 같은 branch를 바라보고 작업할 때 A 개발자가 remote repository에 먼저 commit를 올리고 B 개발자도 동일하게 commit을 만든 상황에서 remote repository에 push를 해야한다면 어떻게 해야 할까?   

바로 push를 할 수는 없기에 pull을 해야 하지만, 이 경우 merge commit이 생기는 문제가 발생한다. 이런 상황에서는 `pull --rebase`를 사용하면 된다.  


```sh
# rebase 옵션을 통해 pull을 하면 remote branch의 commit들을 pull한 후, local branch의 commit들을 그 위에 쌓습니다(rebase)
$ git pull origin {브랜치명} --rebase
```

pull을 할 때 rebase 옵션을 줘서 커밋의 순서를 일정하게 보장해서 push를 바로 진행할 수 있습니다