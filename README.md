# taiwan_stock

This project aims to collect data of Taiwan stock automatically.

# Install
1. mysql
	brew install mysql
 
2. goose
	go get -u github.com/pressly/goose/cmd/goose

3. python3

# Step
1. Create database twse

2. Execute db migration


# Appendix

## 銀行票券業股(COMPB.bnk)之「開頭字母」與「項目名稱英文縮寫」
   http://www.tedc.org.tw/tedc/bank/comp/ch2.4.4.htm

損益表 (Income Statement， 開頭字母 I， 共 25 項)

單位: 新台幣千元
(59)	INTR：利息收入 (Interest Revenue)
(60)	INTE：利息費用 (Interest Expense)
(61)	INTN：利息淨收益 (Interest Income (Net))
　	註：(61)=(59)-(60)
(62)	FEE： 手續費淨收益 (Service Fee Revenue & Commission (Net))
(63)	FIAL：透過損益按公允價值衡量之金融資產及負債損益 (Gains or Losses on Financial Assets (Liabilities) at Fair Value through Profit or Loss)
(64)	REFI：備供出售金融資產之已實現損益 (Realized Gain or Loss on Available-for-sale Financial Assets)
(65)	IIL：採用權益法認列之子公司損益之份額 (Investment Income or Loss from Investment Accounted for Using Equity Method)
(66)	XGL：兌換損益 (Foreign Exchange Gain or Loss)
(67)	AIMP： 資產減損損益 (Loss on Asset Impairment)
(68)	ORES： 其他各項提存 (Provision for Other Reserve)
(69)	NLOAN：攤銷出售不良債權損益 (Amortization Loss (Gain) on Selling of Non-performing Loans)
(70)	PROP：財產交易損益 (Gain or Loss on Property Exchange)
(71)	RBAD：收回呆帳及過期帳 (Recovered Bad & Overdue Accounts)
(72)	OREV：其他非利息淨損益 (Other Revenue Except for Interest Income)
(73)	NREV：淨收益 (Net Revenue)
　	註：(73)=(59)+(60)+(61)+(62)+(63)+(64)+(65)+(66)+(67)+(68)+(69)+(70)+(71)+(72)
(74)	BAD：呆帳費用及保證責任準備提存 (Bad Debt Expense & Guarantee Liability Provisions)
(75)	OE：營業費用 (Operating Expenses)
(76)	BTAX：繼續營業部門稅前淨利 (Income Before Income Tax from Continuing Operations)
 	註：(76)=(73)-(74)-(75)
(77)	TAX：所得稅費用 (Income Tax Expenses)
(78)	CONT：繼續營業部門淨利 (Income from Continuing Operations)
　	註：(78)=(76)-(77)
(79)	DISC：停業部門損益 (Income (Loss) from Discontinued Department)
(80)	EXT：非常損益 (Extraordinary Items)
(81)	ACC：累積影響數 (Change in AAccounting Principles)
(82)	NI：本期稅後淨利 (Net Income)
　	註：(82)=(78)+(79)+(80)+(81)
(83)	EPS：每股盈餘(元) (Earnings Per Share)
	
