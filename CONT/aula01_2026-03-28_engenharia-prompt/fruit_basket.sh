#!/bin/bash

# custo total da cesta de frutas em centavos
COST_PINEAPPLE=50
COST_BANANA=4
COST_WATERMELON=23
COST_BASKET=1

# Calculo do custo total
TOTAL_COST=$((COST_PINEAPPLE + COST_BANANA + COST_WATERMELON + COST_BASKET))

# mostrar o custo total em centavos
echo " O custo total da cesta de frutas é: $TOTAL_COST centavos."