public class Main
{
	public static void main(String[] args) {
	    int s=Integer.parseInt(args[0]);
	    int v1=Integer.parseInt(args[1]);
	    int v2=Integer.parseInt(args[2]);
	    boolean t=true;
	    int x=s/v1; //amount of larger ones
	    int y=s%v1; //ounces left
	    while((y%v2)>0){
	        x--;
	        y+=v1;
	     if(x==0&&((y%v2)>0)){
	         System.out.println("Impossible");
	         t=false;
            } 
	    }
	    if (t){
	    int z= y/v2; //amount of smaller
	    System.out.println(x +","+z);
	    }
	    return;
	    
	}
}
