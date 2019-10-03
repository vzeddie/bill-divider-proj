package billsep_java;

public class Contributor {
	private double base_total = 0.00;
	private double tax = 0.00;
	private double tip = 0.00;
	private String name;
	private double tax_rate;
	private double tip_percentage;

	public Contributor(String name, double tax_rate, double tip_percentage){
		this.name = name;
		this.tax_rate = tax_rate;
		this.tip_percentage = tip_percentage;
	}
	
	public void set_base_total(double new_value){
		this.base_total = new_value;
	}

	public void update_info(){
		this.tax = this.base_total * (this.tax_rate/100 );
		this.tip = this.base_total * (this.tip_percentage/100);
	}

	public void set_name(String new_name){
		this.name = new_name;
	}

	public void print_contributor(){
		update_info();
		System.out.println("Name: " + this.name);
		System.out.println("Base total: " + this.base_total);
		System.out.println("Tax (" + this.tax_rate + "%): " + this.tax);
		System.out.println("Tip (" + this.tip_percentage + "%): " + this.tip);
		System.out.println("Entire total: " + (this.base_total + this.tax + this.tip)); 
	}

}
