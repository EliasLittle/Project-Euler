function dig_sum(base, pow)
	num = big(base) ^ pow
	sum = 0
	while num != 0
		sum += num % 10
		num ÷= 10
	end
	sum
end

function main()
	max = 0
	for I in CartesianIndices((2:100, 2:100))
		val = dig_sum(I[1],I[2])
        	max = val > max ? val : max
	end
	println(max)
end

main()
