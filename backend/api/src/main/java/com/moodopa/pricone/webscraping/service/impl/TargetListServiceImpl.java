package com.moodopa.pricone.webscraping.service.impl;

import com.moodopa.pricone.webscraping.mapper.TargetListMapper;
import com.moodopa.pricone.webscraping.service.TargetListService;
import com.moodopa.pricone.webscraping.vo.TargetListVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
public class TargetListServiceImpl implements TargetListService {
	
	@Autowired
	TargetListMapper mapper;
	
	@Override
	public Map<String, Object> list(TargetListVo paramVo) {
		
		Map<String, Object> retMap = new HashMap<>();
		
		List<TargetListVo> targetListVoList  = mapper.list(paramVo);
		
		retMap.put("code", "200");
		retMap.put("message", "정상적으로 처리되었습니다.");
		retMap.put("data", targetListVoList);
		
		return retMap;
	}
}
