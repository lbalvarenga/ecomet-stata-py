/*
*                    (  )/
*                     )(/
*  ________________  ( /)
* ()__)____________)))))    hjw
* 
* Art by Hayley Jane Wakenshaw
*
* Author: Lucas Alvarenga <lb.am.alvarenga@uel.br>
*   Date: 2024-04-29
*   Desc: Routine to find and analyse correlations
*         between smoking products production and 
*         IT/Financial workers data in Brazil
*         (2012-2024)
*/ qui {

clear all // TODO: Remove after routine is complete

// LOCAL LIST ----
local BASE_PATH "\\wsl.localhost\Debian\home\lal\work\uel\ecomet\4b" // Project folder
local EXEC_BLOCKING 1 // Wait for user input between steps
local SHOW_SCATTER 1  // Show scatter plots



// ROUTINE    ----
cd `BASE_PATH'
do "utils.do" // Helper programs

sysuse auto
import delimited "csv\output.csv", clear // TODO: Remove after routine is complete

// Date handling
gen int year = real(substr(dt, 1, 4))
gen int month = real(substr(dt, 6, 2))
gen _dt = ym(year, month)
format _dt %tm
tsset _dt, monthly

// Regression setup
global ylist smk // Fumo
global xlist occ // Ocupação

if `SHOW_SCATTER' {
	twoway (scatter $ylist $xlist, sort)
	noisily block_prompt `EXEC_BLOCKING'
}

n _print "Regressão"
n regress $ylist $xlist

// Prediction
predict p_smk, xb

if `SHOW_SCATTER' {    
	twoway (scatter $ylist $xlist, sort) (line p_smk $xlist, sort)
	noisily block_prompt `EXEC_BLOCKING'
}

// Dickey-Fuller
n _print "Dickey-Fuller Aumentado"
n dfuller $ylist
n _print "Dickey-Fuller Aumentado com tendência"
n dfuller $ylist, trend


// ARCH, GARCH

// n arch $ylist $xlist, arch(1, 2)

}