public class Test{

    public static void main(String[] args) {
        long num = 0;
        for (int i = 0; i < 10000; i++){
            for (int j = 0; j < 10000; j++){
                num += j;
            }
        }
        
        System.out.println(num);
    }

}