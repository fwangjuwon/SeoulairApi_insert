package site.metacoding.seoulair.web;

import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import lombok.RequiredArgsConstructor;
import site.metacoding.seoulair.domain.Seoulair;
import site.metacoding.seoulair.domain.SeoulairRepository;

@RequiredArgsConstructor
@Controller
public class SeoulairController {

    private final SeoulairRepository seoulairRepository;

    @GetMapping("/weather")
    public String main(Model model) {
        List<Seoulair> seoul = null;

        seoul = seoulairRepository.findAll();

        model.addAttribute("data", seoul);
        return "main";
    }
}
