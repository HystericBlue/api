package com.moodopa.pricone.webscraping;

import com.moodopa.pricone.webscraping.service.TargetListService;
import com.moodopa.pricone.webscraping.vo.TargetListVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.HashMap;
import java.util.Map;

@Controller
@RequestMapping("/webScraping")
public class WebScrapingController {
	
	@Autowired
	TargetListService service;
	
	public Map list(TargetListVo paramVo) {
		
		return new HashMap();
	}
	
}
