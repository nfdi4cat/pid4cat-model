package None;

import java.util.List;
import lombok.*;






/**
  The data element in the handle API for the contact email.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HdlDataContact  {

  private String format;
  private String value;

}
