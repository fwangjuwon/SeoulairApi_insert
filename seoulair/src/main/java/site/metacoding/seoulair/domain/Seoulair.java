package site.metacoding.seoulair.domain;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@AllArgsConstructor
@NoArgsConstructor
@Data
@Entity
public class Seoulair {

    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Id
    private Integer id;

    private String msrdt;
    private String msrrgn_nm;
    private String msrste_nm;
    private String pm10;
    private String pm25;
    private String o3;
    private String no2;
    private String co;
    private String so2;
    private String idex_nm;
    private String idex_mvl;
    private String arplt_main;
}
