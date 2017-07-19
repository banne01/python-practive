'''
private List<Integer> roundSum(List<Double> list) {
		List<Integer> output = new ArrayList<>();
		double deviation = 0;
		double lossroundedup = 0;
		double lossroundeddown = 0;
		for(int i=0;i<list.size();i++) {
			lossroundedup = Math.ceil(list.get(i)) - list.get(i);
			lossroundeddown = Math.floor(list.get(i)) - list.get(i);
			if(Math.abs(deviation+lossroundeddown) < Math.abs(deviation+lossroundedup)) {
				output.add((int)Math.floor(list.get(i)));
				deviation += lossroundeddown; 
			} else {
				output.add((int)Math.ceil(list.get(i)));
				deviation += lossroundedup;
			}
		}
		return output;
	}

'''        
