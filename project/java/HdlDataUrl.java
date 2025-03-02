package None;

import java.util.List;
import lombok.*;






/**
  The data element in the handle API for the redirect url.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HdlDataUrl  {

  private String format;
  private String value;

}
