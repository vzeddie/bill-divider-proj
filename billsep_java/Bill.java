package billsep_java;

public class Bill {
	private double base_total = 0.00;
	private double tax = 0.00;
	private double tip = 0.00;
	private String name;
	private double tax_rate = 8.75;
	private double tip_percentage = 18.00;
	private int num_contributors = 0;

	public Bill(int num_contributors) {
		this.num_contributors = num_contributors;
	}

	public void add_item() {
		
	}
}