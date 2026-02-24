n = 1;
P = 1;
while P > 0.01
    n = n + 1 % Increment n for the next iteration
    Product = 365;
    for i=1:n-1
        Product = Product*(365-i);
    end
    P = Product/365^n % Update P based on the new value of n
end
disp(n)