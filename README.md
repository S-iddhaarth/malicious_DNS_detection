# malicious_DNS_detection

## Feature Vector 

| Feature                                              | Description                                      |
|------------------------------------------------------|--------------------------------------------------|
| NUMBER OF CHARACTERS                                 | Total number of characters in the domain          |
| NUMBER OF DIFFERENT CHARACTERS                        | Number of unique characters in the domain         |
| C                                                    | Count of consonants in the domain                 |
| V                                                    | Count of vowels in the domain                     |
| 1-GRAM MEAN                                          | Mean of character unigram frequencies             |
| 1-GRAM VARIANCE                                      | Variance of character unigram frequencies         |
| 1-GRAM STANDARD DEVIATION                            | Standard deviation of character unigram frequencies|
| 2-GRAM MEAN                                          | Mean of character bigram frequencies              |
| 2-GRAM VARIANCE                                      | Variance of character bigram frequencies          |
| 2-GRAM STANDARD DEVIATION                            | Standard deviation of character bigram frequencies|
| CC                                                   | Count of consecutive consonant pairs              |
| VC                                                   | Count of vowel-consonant pairs                    |
| CV                                                   | Count of consonant-vowel pairs                    |
| CCC                                                  | Count of consecutive consonant triplets           |
| CVC                                                  | Count of consonant-vowel-consonant triplets      |
| VCC                                                  | Count of vowel-consonant-consonant triplets      |
| VCV                                                  | Count of vowel-consonant-vowel triplets           |
| MAX FREAQUECNY CHARTER/TOTAL NUMBER OF CHARACTER     | Ratio of the most frequent character to total characters|
| MIN FREAQUENCY CHARACTER/TOTAL NUMBER OF CHARACTER   | Ratio of the least frequent character to total characters|
| SHANON ENTROPY                                       | Shannon entropy of character frequencies          |
| IN                                                   | Count of occurrences of the substring "IN"        |
| ER                                                   | Count of occurrences of the substring "ER"        |
| AN                                                   | Count of occurrences of the substring "AN"        |
| RE                                                   | Count of occurrences of the substring "RE"        |
| ES                                                   | Count of occurrences of the substring "ES"        |
| AR                                                   | Count of occurrences of the substring "AR"        |
| ON                                                   | Count of occurrences of the substring "ON"        |
| OR                                                   | Count of occurrences of the substring "OR"        |
| TE                                                   | Count of occurrences of the substring "TE"        |
| AL                                                   | Count of occurrences of the substring "AL"        |
| ST                                                   | Count of occurrences of the substring "ST"        |
| NE                                                   | Count of occurrences of the substring "NE"        |
| EN                                                   | Count of occurrences of the substring "EN"        |
| ING                                                  | Count of occurrences of the substring "ING"       |
| ION                                                  | Count of occurrences of the substring "ION"       |
| INE                                                  | Count of occurrences of the substring "INE"       |
| TER                                                  | Count of occurrences of the substring "TER"       |
| LIN                                                  | Count of occurrences of the substring "LIN"       |
| ENT                                                  | Count of occurrences of the substring "ENT"       |
| THE                                                  | Count of occurrences of the substring "THE"       |
| ERS                                                  | Count of occurrences of the substring "ERS"       |
| AND                                                  | Count of occurrences of the substring "AND"       |
| EST                                                  | Count of occurrences of the substring "EST"       |
| TIO                                                  | Count of occurrences of the substring "TIO"       |
| TRA                                                  | Count of occurrences of the substring "TRA"       |
| TOR                                                  | Count of occurrences of the substring "TOR"       |
| ART                                                  | Count of occurrences of the substring "ART"       |

## Dependencies
here are list of libraries that you need to install along with terminal command for .venv environment
```shell
$ pip install numpy
```  
```shell
$ pip install scikit-learn
```  
```shell
$ pip install scapy
```  
```shell
$ pip install joblib
```  
```
$ pip install pandas
```
### Run the code from "main" directory. main.py is used to train the data. dns_capture.py is used to flag dns from real time network traffic