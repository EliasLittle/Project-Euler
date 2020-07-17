function fac(x::Int)::Int
    ans = 1
    while x != 1
        ans*=x
        x-=1
    end
    return ans
end

function f(x::Int)::Int
    sum = 0
    for i in digits(x,base=10)
        sum += fac(i)
    end
    return sum
end

loops = Dict(169 => 3,363601 => 3, 1454 => 3, 871 => 2, 872 => 2, 45361 => 2, 45362 => 2, 145 => 1, 1 => 1, 2 => 1)

function chain(num::Int)::Int
    seen = []
    next = f(num)
    len = 1
    println("Begining Iteration")
    while !haskey(loops,next) && next !== num
        println("In while loop")
        len += 1
        println("Finding Next")
        temp = f(next)
        next = temp
        println("Found Next")
        println(next)
    end

    println("Found Stopping Point")

    seen_len = size(seen,1)
    for i in seen_len:1
        loops[seen[i]] = len-(seen_len-i-1)
    end

    return haskey(loops,next) ? len+loops[next] : len
end

k = 69
next = f(k)
println(next)
while next !== k
    next = f(next)
    println(next)
end
#println(f(69))
#println(chain(69))
println("Ended")
