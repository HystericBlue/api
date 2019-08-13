package com.moodopa.pricone.webscraping.mapper;

import com.moodopa.pricone.webscraping.vo.TargetListVo;

import java.util.List;

public interface TargetListMapper {
	
	List<TargetListVo> list(TargetListVo targetList);
}
