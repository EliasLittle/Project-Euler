# SOLVED

function next(v̄,φ)
  φ⁻ = 1/φ
  φᵣ,φᵢ = modf(φ⁻)
  push!(v̄,BigInt(φᵢ))
  return φᵣ
end

function frac_sum(v̄)
  if length(v̄) == 1
    return v̄[1]
  end
  return v̄[1]+one(BigInt)//frac_sum(v̄[2:end])
end

function pell(d)
  if  Int(floor(√d))^2 == d
    return (0,0)
  end
  h,k = 1,1
  γ,I = modf(√d)
  v=[BigInt(I)]
  while h^2 - d * k^2 != 1
    γ = next(v,γ)
    rt = frac_sum(v)
    h,k = numerator(rt),denominator(rt)
  end
  return (h,k)
end


X = (one(BigInt),1)
for d in 2:1000
  global X
  b = pell(BigInt(d))
  if b[1] > X[1]
    X = (b[1],d)
  end
  println(d," : ", b)
end

println("Max: ", X)
