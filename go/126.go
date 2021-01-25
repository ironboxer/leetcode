/*

https://leetcode.com/problems/word-ladder-ii/

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

*/

package main


import "fmt"


/*
func dictIn(dict map[string]bool, target string) bool {
    _, ok := dict[target]
    return  ok
}


func sliceAdd(slice []string, val string) []string {
    buf := make([]string, len(slice) + 1)
    copy(buf, slice)
    buf[len(slice)] = val
    return buf
}


type Node struct {
    Word string
    Path []string
}


func findLadders(beginWord string, endWord string, wordList []string) [][]string {
    res := make([][]string, 0)
    wordDict := make(map[string]bool, len(wordList))
    for i := 0; i < len(wordList); i++ {
        wordDict[wordList[i]] = true
    }
    if !dictIn(wordDict, endWord) {
        return res
    }
    ch := make([]string, 26)
    for i := 0; i < 26; i++ {
        ch[i] = string(byte(i) + 'a')
    }
    path := make([]string, 0)
    path = append(path, beginWord)
    root := &Node{Word: beginWord, Path: path} 
    queue := make([]*Node, 0)
    queue = append(queue, root)
    for len(queue) > 0 {
        node := queue[0]
        queue = queue[1:]
        word := node.Word
        path := node.Path
        if word == endWord {
            res = append(res, path)
            continue
        }
        rmWords := make([]string, 0)
        for i := 0; i < len(word); i++ {
            for _, c := range ch {
                newWord := word[:i] + c + word[i+1:]
                if dictIn(wordDict, newWord) {
                    newPath := sliceAdd(path, newWord)
                    newNode := &Node{Word: newWord, Path: newPath}
                    queue = append(queue, newNode)
                    rmWords = append(rmWords, newWord)
                }
            }
        }
        for i := 0; i < len(rmWords); i++ {
            delete(wordDict, rmWords[i])
        }
    }
    return res
}
*/


// 126, 127 是不一样的思路?


func sliceAdd(slice []string, val string) []string {
    buf := make([]string, len(slice) + 1)
    copy(buf, slice)
    buf[len(slice)] = val
    return buf
}


func sliceMerge(s1 [][]string, s2 [][]string) [][]string {
    s := make([][]string, 0)
    for _, l := range s1 {
        s = append(s, l)
    }
    for _, l := range s2 {
        s = append(s, l)
    }
    return s
}


func findLadders(beginWord string, endWord string, wordList []string) [][]string {
    var res [][]string
    wordDict := make(map[string]bool)
    for _, w := range wordList {
        wordDict[w] = true
    }
    if _, ok := wordDict[endWord]; !ok {
        return res
    }
    ch := make([]string, 26)
    for i := 0; i < 26; i++ {
        ch[i] = string(byte(i) + 'a')
    }
    layer := make(map[string][][]string)
    layer[beginWord] = make([][]string, 0)
    beginList := make([]string, 0)
    beginList = append(beginList, beginWord)
    layer[beginWord] = append(layer[beginWord], beginList)
    for len(layer) > 0 {
        newLayer := make(map[string][][]string)
        for word, list := range layer {
            if word == endWord {
                return list
            }
            for i := 0; i < len(word); i++ {
                for _, c := range ch {
                    newWord := word[:i] + c + word[i+1:]
                    if _, ok := wordDict[newWord]; ok {
                        newList := make([][]string, 0)
                        for j := 0; j < len(list); j++ {
                            subList := sliceAdd(list[j], newWord)
                            newList = append(newList, subList)
                        }
                        newLayer[newWord] = sliceMerge(newLayer[newWord], newList)
                    }
                }
            }
        }
        for k, _ := range newLayer {
            delete(wordDict, k)
        }
        layer = newLayer
    }
    return res
}

// 只能说这个算法是目前比较好的

func main() {
    beginWord := "hit"
    endWord := "cog"
    wordList := []string{"hot","dot","dog","lot","log","cog"}
    fmt.Println(findLadders(beginWord, endWord, wordList))


    beginWord = "hit"
    endWord = "cog"
    wordList = []string{"hot","dot","dog","lot","log"}
    fmt.Println(findLadders(beginWord, endWord, wordList)) 
    beginWord = "cet"
    endWord = "ism"
    wordList = []string{"kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"}
    fmt.Println(findLadders(beginWord, endWord, wordList))
}

