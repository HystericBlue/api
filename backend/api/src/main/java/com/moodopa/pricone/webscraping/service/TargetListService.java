package com.moodopa.pricone.webscraping.service;

import com.moodopa.pricone.webscraping.vo.TargetListVo;

import java.util.Map;

public interface TargetListService {
	
	Map<String, Object> list(TargetListVo targetListVo);
	
}
