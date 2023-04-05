use "./../../../mysmlib/mysmlib-cls.sml";

fun stream_cycling_list(xs: 'a list): 'a stream = fn() => 
    let
        fun cycle (x::xs) = strcon_cons (x, fn() => cycle (xs @ [x]))
          | cycle [] = strcon_nil
    in
        cycle xs
        
    end


val xs = [1, 2, 3, 4, 5];
val ys = stream_cycling_list xs;